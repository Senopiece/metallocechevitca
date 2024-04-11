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
	city_id: number;
	images: number[];
}

export interface PlacePrediction {
	XID: string;
	Name: string;
	Lon: number;
	Lat: number;
	probability: number;
}

export interface TextQueryResponse {
	places: PlacePrediction[];
}
