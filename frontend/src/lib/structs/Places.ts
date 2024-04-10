export interface Area {
	id: number;
	name: string;
}

export interface CategoryPrediction {
	category: string;
	probability: number;
}

export interface LatLon {
	Lat: number;
	Lon: number;
}

export interface ImageQueryResponse {
	optimal_route: LatLon[] | null;
	places: PlacePrediction[];
	categories: CategoryPrediction[];
}

export interface PlaceInfo {
	category: string;
	images: string[];
}

export interface PlacePrediction {
	XID: string;
	Name: string;
	Lon: number;
	Lat: number;
	city_id: number;
	probability: number;
}

export interface TextQueryResponse {
	optimal_route: LatLon[] | null;
	places: PlacePrediction[];
}
