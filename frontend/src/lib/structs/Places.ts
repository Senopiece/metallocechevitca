interface Area {
  id: number;
  name: string;
}

interface CategoryPrediction {
  category: string;
  probability: number;
}

interface ImageQueryResponse {
  places: PlacePrediction[];
  categories: CategoryPrediction[];
}

interface PlaceInfo {
  category: string;
  city_id: number;
  images: number[];
}

interface PlacePrediction {
  XID: string;
  Name: string;
  Lon: number;
  Lat: number;
  probability: number;
}

interface TextQueryResponse {
  places: PlacePrediction[];
}
