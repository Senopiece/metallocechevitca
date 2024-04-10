export interface MultimodalSelectedText {
	type: 'text';
	value: string;
}

export interface MultimodalSelectedFile {
	type: 'image';
	file: File;
}

export type MultimodalSelected = MultimodalSelectedText | MultimodalSelectedFile;
