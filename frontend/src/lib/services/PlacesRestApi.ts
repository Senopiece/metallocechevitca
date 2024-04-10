import axios, { type AxiosInstance } from 'axios';
import type { Places } from './Places';
import type { Area, ImageQueryResponse, PlaceInfo, TextQueryResponse } from '$lib/structs/Places';

export class PlacesRestApi implements Places {
	private axiosInstance: AxiosInstance;

	constructor(baseUrl: string) {
		this.axiosInstance = axios.create({
			baseURL: baseUrl
		});
	}

	async getAreas() {
		const response = await this.axiosInstance.get<Area[]>('/info/areas/');
		return response.data;
	}

	async searchText(query: string, areasId: number[], placesLimit: number = 5) {
		const response = await this.axiosInstance.get<TextQueryResponse>('/search/text/', {
			params: {
				query,
				areas_id: areasId,
				places_limit: placesLimit
			}
		});
		return response.data;
	}

	async searchImage(areasId: number[], imageFile: File, placesLimit: number = 5) {
		const formData = new FormData();
		formData.append('image_file', imageFile);

		// Axios will automatically set the Content-Type to 'multipart/form-data'
		const response = await this.axiosInstance.put<ImageQueryResponse>('/search/image/', formData, {
			params: {
				places_limit: placesLimit,
				// Passing array parameters in queries with Axios correctly formats them for the server
				'areas_id[]': areasId
			}
		});

		return response.data;
	}

	async getPlaceInfo(xid: string) {
		const response = await this.axiosInstance.get<PlaceInfo>(`/place/${xid}`);
		return response.data;
	}
}
