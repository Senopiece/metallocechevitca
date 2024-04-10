export interface Area {
	id: number;
	name: string;
}

export interface CategoryPrediction {
	category: string;
	probability: number;
}

export interface ImageQueryResponse {
	places: PlacePrediction[];
	categories: CategoryPrediction[];
}

export interface PlaceInfo {
	category: string;
	images: number[];
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
	places: PlacePrediction[];
}
