import { PlacesRestApi } from './PlacesRestApi';
import { env } from '$env/dynamic/public';
import type { Area, ImageQueryResponse, PlaceInfo, TextQueryResponse } from '$lib/structs/Places';

export interface Places {
	getAreas(): Promise<Area[]>;
	searchText(query: string, areasId: number[], placesLimit?: number): Promise<TextQueryResponse>;
	searchImage(
		areasId: number[],
		imageFile: File,
		placesLimit?: number
	): Promise<ImageQueryResponse>;
	getPlaceInfo(xid: string): Promise<PlaceInfo>;
}

export function getPlacesApiPath(): string {
	return env.PUBLIC_PLACES_REST_API_URL || 'http://localhost';
}

export function getPlacesImpl(): Places {
	return new PlacesRestApi(getPlacesApiPath());
}
