/*
 * eos - A 3D Morphable Model fitting library written in modern C++11/14.
 *
 * File: include/eos/fitting/contour_correspondence.hpp
 *
 * Copyright 2015, 2016 Patrik Huber
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#pragma once

#ifndef CONTOURCORRESPONDENCE_HPP_
#define CONTOURCORRESPONDENCE_HPP_

#include "eos/core/Landmark.hpp"
#include "eos/core/Mesh.hpp"

#include "cereal/archives/json.hpp"

#include "glm/gtc/matrix_transform.hpp"

#include "Eigen/Core"

#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <tuple>

namespace eos {
	namespace fitting {

// Forward declarations of later used functions and types:
struct ModelContour;
struct ContourLandmarks;
std::pair<std::vector<std::string>, std::vector<int>> select_contour(float yaw_angle, const ContourLandmarks& contour_landmarks, const ModelContour& model_contour);
std::tuple<std::vector<Eigen::Vector2f>, std::vector<Eigen::Vector4f>, std::vector<int>> get_nearest_contour_correspondences(const core::LandmarkCollection<Eigen::Vector2f>& landmarks, const std::vector<std::string>& landmark_contour_identifiers, const std::vector<int>& model_contour_indices, const core::Mesh& mesh, const glm::mat4x4& view_model, const glm::mat4x4& ortho_projection, const glm::vec4& viewport);


/**
 * @brief Definition of the vertex indices that define the right and left model contour.
 *
 * This class holds definitions for the contour (outline) on the right and left
 * side of the reference 3D face model. These can be found in the file
 * share/model_contours.json. The Surrey model's boundaries are conveniently
 * approximately located near the actual 2D image contour, for the front-facing
 * contour.
 *
 * Note: We should extend that to the 1724 model to get a few more points, this
 * should improve the contour fitting.
 */
struct ModelContour
{
	// starting from right side, eyebrow-height: (I think the order matters here)
	std::vector<int> right_contour;
	/* 23 = middle, below chin - not included in the contour here */
	// starting from left side, eyebrow-height:
	std::vector<int> left_contour;

	// We store r/l separately because we currently only fit to the contour facing the camera.
	// Also if we were to fit to the whole contour: Be careful not to just fit to the closest. The 
	// "invisible" ones behind might be closer on an e.g 90� angle. Store CNT for left/right side separately?
	
	/**
	 * Helper method to load a ModelContour from
	 * a json file from the hard drive.
	 *
	 * Eventually, it might be included in the MorphableModel class.
	 *
	 * @param[in] filename Filename to a model.
	 * @return The loaded ModelContour.
	 * @throw std::runtime_error When the file given in \c filename fails to be opened (most likely because the file doesn't exist).
	 */
	static ModelContour load(std::string filename)
	{
		ModelContour contour;

		std::ifstream file(filename);
		if (file.fail()) {
			throw std::runtime_error("Error opening given file: " + filename);
		}
		cereal::JSONInputArchive input_archive(file);
		input_archive(contour);

		return contour;
	};

	friend class cereal::access;
	/**
	 * Serialises this class using cereal.
	 *
	 * @param[in] archive The archive to serialise to (or to serialise from).
	 */
	template<class Archive>
	void serialize(Archive& archive)
	{
		archive(cereal::make_nvp("right_contour", right_contour), cereal::make_nvp("left_contour", left_contour));
	};
};

/**
 * @brief Defines which 2D landmarks comprise the right and left face contour.
 *
 * This class holds 2D image contour landmark information. More specifically,
 * it defines which 2D landmark IDs correspond to the right contour and which
 * to the left. These definitions are loaded from a file, for example from
 * the "contour_landmarks" part of share/ibug_to_sfm.txt.
 * 
 * Todo: We should improve error handling here. When there's no contour_landmarks
 * in the file, it will crash, but it would be nice if it still worked, the returned
 * vectors should just be empty.
 *
 * Note: Better names could be ContourDefinition or ImageContourLandmarks, to
 * disambiguate 3D and 2D landmarks?
 * Todo: I think this should go into the LandmarkMapper. Isn't it part of ibug_to_sfm.txt already?
 */
struct ContourLandmarks
{
	// starting from right side, eyebrow-height.
	std::vector<std::string> right_contour;
	// Chin point is not included in the contour here.
	// starting from left side, eyebrow-height. Order doesn't matter here.
	std::vector<std::string> left_contour;

	// Note: We store r/l separately because we currently only fit to the contour facing the camera.
	
	/**
	 * Helper method to load contour landmarks from a text file with landmark
	 * mappings, like ibug_to_sfm.txt.
	 *
	 * @param[in] filename Filename to a landmark-mapping file.
	 * @return A ContourLandmarks instance with loaded 2D contour landmarks.
	 * @throw std::runtime_error When the file given in \c filename fails to be opened (most likely because the file doesn't exist).
	 */
	static ContourLandmarks load(std::string filename)
	{
		using std::string;
		using std::getline;

		ContourLandmarks contour;

		std::ifstream file(filename);
		if (!file.is_open()) {
			throw std::runtime_error(string("ContourLandmarks: Could not open landmark mappings file: " + filename));
		}

		// We'll need these helper functions for the parsing:
		auto starts_with = [](const std::string& input, const std::string& match)
		{
			return input.size() >= match.size() && std::equal(match.begin(), match.end(), input.begin());
		};

		auto trim_left = [](const std::string& input, std::string pattern = " \t")
		{
			auto first = input.find_first_not_of(pattern);
			if (first == std::string::npos)
			{
				return input;
			}
			return input.substr(first, input.size());
		};

		// Read the actual file:
		string line;
		// Skip any comments (";") or empty lines at the beginning:
		while (getline(file, line)) {
			if (!starts_with(line, ";") && line != "")
			{
				// not a commented or not an empty line
				break;
			}
		}
		// First actual line should be "landmarkMappings"
		if (!starts_with(line, "landmarkMappings")) {
			throw std::runtime_error("ContourLandmarks error: First non-comment line should be \"landmarkMappings\".");
		}
		getline(file, line);
		// The next line has to be "{":
		if (line != "{") {
			throw std::runtime_error("ContourLandmarks error: Expected a \"{\" on the line following the \"landmarkMappings\" statement.");
		}
		// Skip the whole landmarkMappings block:
		while (getline(file, line))
		{
			if (line == "}") { // end of the block
				break;
			}
		}

		// Next actual line should be "contour_landmarks":
		getline(file, line);
		if (!starts_with(line, "contour_landmarks")) {
			throw std::runtime_error("ContourLandmarks error: Expected a \"contour_landmarks\" block.");
		}
		getline(file, line);
		// The next line has to be "{":
		if (line != "{") {
			throw std::runtime_error("ContourLandmarks error: Expected a \"{\" on the line following the \"contour_landmarks\" statement.");
		}
		getline(file, line);
		// The next line has to be "right {":
		if (trim_left(line) != "right {") {
			throw std::runtime_error("ContourLandmarks error: Expected a line containing \"right {\".");
		}
		// Now read all the "right" contour landmarks:
		while (getline(file, line))
		{
			if (trim_left(line) == "}") { // end of the block
				break;
			}
			// on comment, continue:
			if (starts_with(trim_left(line), ";"))
			{
				continue;
			}
			std::stringstream line_stream(line);
			string value;
			if (!(line_stream >> value)) {
				throw std::runtime_error(string("Contour landmarks format error while parsing the line: " + line));
			}
			contour.right_contour.push_back(value);
		}
		// The next line has to be "left {":
		getline(file, line);
		if (trim_left(line) != "left {") {
			throw std::runtime_error("ContourLandmarks error: Expected a line containing \"left {\".");
		}
		// Now read all the "left" contour landmarks:
		while (getline(file, line))
		{
			if (trim_left(line) == "}") { // end of the block
				break;
			}
			// on comment, continue:
			if (starts_with(trim_left(line), ";"))
			{
				continue;
			}
			std::stringstream line_stream(line);
			string value;
			if (!(line_stream >> value)) {
				throw std::runtime_error(string("Contour landmarks format error while parsing the line: " + line));
			}
			contour.left_contour.push_back(value);
		}
		getline(file, line);
		// The last line has to be the "}" closing the contour_landmarks block:
		if (line != "}") {
			throw std::runtime_error("ContourLandmarks error: Expected a line containing \"}\".");
		}

		return contour;
	};
};

/**
 * Given a set of 2D image landmarks, finds the closest (in a L2 sense) 3D vertex
 * from a list of vertices pre-defined in \p model_contour. \p landmarks can contain
 * all landmarks, and the function will sub-select the relevant contour landmarks with
 * the help of the given \p contour_landmarks. This function choses the front-facing
 * contour and only fits this contour to the 3D model, since these correspondences
 * are approximately static and do not move with changing pose-angle.
 *
 * It's the main contour fitting function that calls all other functions.
 *
 * Note: Maybe rename to find_contour_correspondences, to highlight that there is (potentially a lot) computational cost involved?
 * Note: Does ortho_projection have to be specifically orthographic? Otherwise, if it works with perspective too, rename to just "projection".
 *
 * @param[in] landmarks All image landmarks.
 * @param[in] contour_landmarks 2D image contour ids of left or right side (for example for ibug landmarks).
 * @param[in] model_contour The model contour indices that should be considered to find the closest corresponding 3D vertex.
 * @param[in] yaw_angle Yaw angle of the current fitting, in degrees. The front-facing contour will be chosen depending on this yaw angle.
 * @param[in] mesh The mesh that's used to find the nearest contour points.
 * @param[in] view_model Model-view matrix of the current fitting to project the 3D model vertices to 2D.
 * @param[in] ortho_projection Projection matrix to project the 3D model vertices to 2D.
 * @param[in] viewport Current viewport to use.
 * @return A tuple with the 2D contour landmark points, the corresponding points in the 3D shape model and their vertex indices.
 */
inline std::tuple<std::vector<Eigen::Vector2f>, std::vector<Eigen::Vector4f>, std::vector<int>> get_contour_correspondences(const core::LandmarkCollection<Eigen::Vector2f>& landmarks, const ContourLandmarks& contour_landmarks, const ModelContour& model_contour, float yaw_angle, const core::Mesh& mesh, const glm::mat4x4& view_model, const glm::mat4x4& ortho_projection, const glm::vec4& viewport)
{
	// Select which side of the contour we'll use:
	std::vector<int> model_contour_indices;
	std::vector<std::string> landmark_contour_identifiers;
	std::tie(landmark_contour_identifiers, model_contour_indices) = select_contour(yaw_angle, contour_landmarks, model_contour);

	// For each 2D contour landmark, get the corresponding 3D vertex point and vertex id:
	// Note/Todo: Loop here instead of calling this function where we have no idea what it's doing? What does its documentation say?
	return get_nearest_contour_correspondences(landmarks, landmark_contour_identifiers, model_contour_indices, mesh, view_model, ortho_projection, viewport);
};

/**
 * Takes a set of 2D and 3D contour landmarks and a yaw angle and returns two
 * vectors with either the right or the left 2D and 3D contour indices. This
 * function does not establish correspondence between the 2D and 3D landmarks,
 * it just selects the front-facing contour. The two returned vectors can thus
 * have different size. 
 * Correspondence can be established using get_nearest_contour_correspondences().
 *
 * If the yaw angle is between +-7.5�, both contours will be selected.
 *
 * Note: Maybe rename to find_nearest_contour_points, to highlight that there is (potentially a lot) computational cost involved?
 *
 * @param[in] yaw_angle Yaw angle in degrees.
 * @param[in] contour_landmarks 2D image contour ids of left or right side (for example for ibug landmarks).
 * @param[in] model_contour The model contour indices that should be used/considered to find the closest corresponding 3D vertex.
 * @return A pair with two vectors containing the selected 2D image contour landmark ids and the 3D model contour indices.
 */
inline std::pair<std::vector<std::string>, std::vector<int>> select_contour(float yaw_angle, const ContourLandmarks& contour_landmarks, const ModelContour& model_contour)
{
	using std::begin;
	using std::end;
	std::vector<int> model_contour_indices;
	std::vector<std::string> contour_landmark_identifiers;
	if (yaw_angle >= -7.5f) { // positive yaw = subject looking to the left
		// ==> we use the right cnt-lms
		model_contour_indices.insert(end(model_contour_indices), begin(model_contour.right_contour), end(model_contour.right_contour));
		contour_landmark_identifiers.insert(end(contour_landmark_identifiers), begin(contour_landmarks.right_contour), end(contour_landmarks.right_contour));
	}
	if (yaw_angle <= 7.5f) {
		// ==> we use the left cnt-lms
		model_contour_indices.insert(end(model_contour_indices), begin(model_contour.left_contour), end(model_contour.left_contour));
		contour_landmark_identifiers.insert(end(contour_landmark_identifiers), begin(contour_landmarks.left_contour), end(contour_landmarks.left_contour));
	}
	// Note there's an overlap between the angles - if a subject is between +- 7.5�, both contours get added.
	return std::make_pair(contour_landmark_identifiers, model_contour_indices);
};

/**
 * Given a set of 2D image landmarks, finds the closest (in a L2 sense) 3D vertex
 * from a list of vertices pre-defined in \p model_contour. Assumes to be given
 * contour correspondences of the front-facing contour.
 *
 * Note: Maybe rename to find_nearest_contour_points, to highlight that there is (potentially a lot) computational cost involved?
 * Note: Does ortho_projection have to be specifically orthographic? Otherwise, if it works with perspective too, rename to just "projection".
 * Note: Actually, only return the vertex id, not the model point as well? Same with get_corresponding_pointset?
 *
 * @param[in] landmarks All image landmarks.
 * @param[in] landmark_contour_identifiers 2D image contour ids of left or right side (for example for ibug landmarks).
 * @param[in] model_contour_indices The model contour indices that should be considered to find the closest corresponding 3D vertex.
 * @param[in] mesh The mesh that's projected to find the nearest contour vertex.
 * @param[in] view_model Model-view matrix of the current fitting to project the 3D model vertices to 2D.
 * @param[in] ortho_projection Projection matrix to project the 3D model vertices to 2D.
 * @param[in] viewport Current viewport to use.
 * @return A tuple with the 2D contour landmark points, the corresponding points in the 3D shape model and their vertex indices.
 */
inline std::tuple<std::vector<Eigen::Vector2f>, std::vector<Eigen::Vector4f>, std::vector<int>> get_nearest_contour_correspondences(const core::LandmarkCollection<Eigen::Vector2f>& landmarks, const std::vector<std::string>& landmark_contour_identifiers, const std::vector<int>& model_contour_indices, const core::Mesh& mesh, const glm::mat4x4& view_model, const glm::mat4x4& ortho_projection, const glm::vec4& viewport)
{
	// These are the additional contour-correspondences we're going to find and then use!
	std::vector<Eigen::Vector4f> model_points_cnt; // the points in the 3D shape model
	std::vector<int> vertex_indices_cnt; // their vertex indices
	std::vector<Eigen::Vector2f> image_points_cnt; // the corresponding 2D landmark points

	// For each 2D-CNT-LM, find the closest 3DMM-CNT-LM and add to correspondences:
	// Note: If we were to do this for all 3DMM vertices, then ray-casting (i.e. glm::unproject) would be quicker to find the closest vertex)
	for (auto&& ibug_idx : landmark_contour_identifiers)
	{
		// Check if the contour landmark is amongst the landmarks given to us (from detector or ground truth):
		// (Note: Alternatively, we could filter landmarks beforehand and then just loop over landmarks => means one less function param here. Separate filtering from actual algorithm.)
		auto result = std::find_if(begin(landmarks), end(landmarks), [&ibug_idx](auto&& e) { return e.name == ibug_idx; }); // => this can go outside the loop
		// TODO Check for ::end!!! if it's not found!
		auto screen_point_2d_contour_landmark = result->coordinates;

		std::vector<float> distances_2d;
		for (auto&& model_contour_vertex_idx : model_contour_indices) // we could actually pre-project them, i.e. only project them once, not for each landmark newly...
		{
			auto vertex = mesh.vertices[model_contour_vertex_idx];
			glm::vec3 proj = glm::project(glm::vec3(vertex), view_model, ortho_projection, viewport);
			Eigen::Vector2f screen_point_model_contour(proj.x, proj.y);

			const double dist = (screen_point_model_contour - screen_point_2d_contour_landmark).norm();
			distances_2d.emplace_back(dist);
		}
		auto min_ele = std::min_element(begin(distances_2d), end(distances_2d));
		// Todo: Cover the case when cnt_indices_to_use.size() is 0.
		auto min_ele_idx = std::distance(begin(distances_2d), min_ele);
		auto the_3dmm_vertex_id_that_is_closest = model_contour_indices[min_ele_idx];

		Eigen::Vector4f vertex(mesh.vertices[the_3dmm_vertex_id_that_is_closest].x, mesh.vertices[the_3dmm_vertex_id_that_is_closest].y, mesh.vertices[the_3dmm_vertex_id_that_is_closest].z, mesh.vertices[the_3dmm_vertex_id_that_is_closest].w);
		model_points_cnt.emplace_back(vertex);
		vertex_indices_cnt.emplace_back(the_3dmm_vertex_id_that_is_closest);
		image_points_cnt.emplace_back(screen_point_2d_contour_landmark);
	}

	return std::make_tuple(image_points_cnt, model_points_cnt, vertex_indices_cnt);
};

	} /* namespace fitting */
} /* namespace eos */

#endif /* CONTOURCORRESPONDENCE_HPP_ */
