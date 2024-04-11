import type { ImageQueryResponse, TextQueryResponse } from './Places';

export interface SearchResultsStoreImage {
	type: 'image';
	image: File;
	res: ImageQueryResponse;
}

export interface SearchResultsStoreText {
	type: 'text';
	res: TextQueryResponse;
}

export type SearchResultsStore = SearchResultsStoreImage | SearchResultsStoreText;
