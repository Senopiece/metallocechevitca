<script lang="ts">
	import type { MultimodalSelected } from '$lib/structs/MultimodalSelect';
	import { createEventDispatcher, onMount } from 'svelte';
	let text = '';
	let imageFile: File | null = null;
	let imagePreviewUrl: null | string = null;
	const dispatch = createEventDispatcher<{
		selected: MultimodalSelected;
	}>();
	let inputMode = 'image'; // Possible values: 'text', 'image'
	let isDraggingOver = false; // Tracks drag state

	function switchInputMode() {
		if (inputMode === 'text') {
			inputMode = 'image';
			if (text) {
				// If switching away from text mode and there is text, dispatch it
				dispatch('selected', { type: 'text', value: text });
			}
			text = ''; // Clear text when switching to image input
		} else {
			inputMode = 'text';
			if (imageFile) {
				// If switching away from image mode and there is an image file, dispatch it
				dispatch('selected', { type: 'image', file: imageFile });
			}
			// Clear image information when switching back to text input
			imageFile = null;
			imagePreviewUrl = null;
		}
	}

	function processFile(file: File) {
		if (file && file.type.startsWith('image/')) {
			imageFile = file;
			imagePreviewUrl = URL.createObjectURL(file);
			dispatch('selected', { type: 'image', file });
		}
	}

	function handleImageChange(event) {
		const file = event.target.files[0];
		processFile(file);
	}

	function handleDragOver(event) {
		event.preventDefault();
	}

	function handleDrop(event) {
		event.preventDefault();
		const file = event.dataTransfer.files[0];
		processFile(file);
		isDraggingOver = false; // Reset drag over state
	}

	function handleDragEnter(event) {
		event.preventDefault();
		isDraggingOver = true;
	}

	function handleDragLeave(event) {
		event.preventDefault();
		isDraggingOver = false;
	}

	$: if (text && inputMode === 'text') {
		dispatch('selected', { type: 'text', value: text });
	}
</script>

<div class="input-wrapper">
	{#if inputMode === 'text'}
		<div class="text-input-box">
			<button
				class="icon-button switch-button"
				on:click={switchInputMode}
				title="Switch to Image Input"
			>
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
					<circle cx="8.5" cy="8.5" r="1.5"></circle>
					<polyline points="21 15 16 10 5 21"></polyline>
				</svg>
			</button>
			<div class="text-input-container">
				<input
					type="text"
					placeholder="Введите описание места"
					bind:value={text}
					class="text-input"
				/>
				<button class="icon-button search-button" title="Search">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<circle cx="11" cy="11" r="8"></circle>
						<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
					</svg>
				</button>
			</div>
		</div>
	{:else}
		<input
			type="file"
			accept="image/*"
			capture="environment"
			id="fileInput"
			on:change={handleImageChange}
			hidden
		/>
		<label
			for="fileInput"
			class="drop-zone"
			on:dragover={handleDragOver}
			on:drop={handleDrop}
			on:dragenter={handleDragEnter}
			on:dragleave={handleDragLeave}
			class:drag-over={isDraggingOver}
		>
			<div class="image-preview-container">
				{#if imagePreviewUrl}
					<img class="preview-img" src={imagePreviewUrl} alt="Image preview" />
				{:else}
					<div class="image-placeholder"></div>
				{/if}
			</div>
			Перетащите изображение сюда или<br /> нажмите чтобы загрузить из проводника
		</label>
		<button
			class="icon-button switch-button"
			on:click={switchInputMode}
			title="Switch to Text Input"
		>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M5 4h14a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"></path>
				<polyline points="12 10 12 14"></polyline>
				<line x1="10" y1="12" x2="14" y2="12"></line>
			</svg>
		</button>
	{/if}
</div>

<style>
	.input-wrapper {
		display: flex;
		flex-direction: column;
		align-items: center;
		font-family: sans-serif;
		width: 100%;
		max-width: 500px; /* Adjust this to fit your design */
	}

	.text-input-box {
		display: flex;
		width: 100%;
		align-items: center;
		justify-content: space-between;
		gap: 10px;
		margin-bottom: 20px;
	}

	.text-input-container {
		display: flex;
		align-items: center;
		position: relative;
		flex-grow: 1;
		background-color: #f0f0f0; /* Light background for the input area */
		border: 2px solid #ccc; /* Light grey border for a flat look */
		border-radius: 5px; /* Slightly rounded corners for aesthetics */
	}

	.text-input {
		flex-grow: 1;
		padding: 10px;
		font-size: 16px;
		border: none; /* Removing individual input border for a unified look */
		border-radius: 5px;
		outline: none;
		background-color: transparent; /* Ensure the background matches the container */
	}

	.text-input:focus {
		border-color: #007bff;
	}

	.icon-button {
		background: none;
		border: none;
		cursor: pointer;
		padding: 8px;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #333; /* Icon color for visibility */
	}

	.icon-button svg {
		height: 24px; /* Adjust size as needed */
		width: 24px;
		stroke: #333; /* Icon color */
	}

	.drop-zone {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		gap: 20px;
		border: 2px dashed #ccc;
		border-radius: 5px;
		padding: 20px;
		text-align: left;
		color: #ccc;
		transition:
			border-color 0.3s,
			color 0.3s;
		width: 100%;
		min-height: 120px; /* Minimum height to accommodate the placeholder */
	}

	.drop-zone.drag-over {
		border-color: #007bff;
		color: #007bff;
	}

	.image-preview-container {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100px; /* Fixed width for the preview */
		height: 100px; /* Fixed height for the preview */
		background-color: #f0f0f0; /* Placeholder color */
		border: 2px dashed #ccc; /* Placeholder border style */
		position: relative; /* Allows precise control over the image and placeholder positioning */
	}

	.preview-img,
	.image-placeholder {
		max-width: 100%;
		max-height: 100%;
		object-fit: cover;
	}

	.image-placeholder {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
		background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>');
		background-repeat: no-repeat;
		background-position: center;
		background-size: 50%; /* Adjust the placeholder icon size */
	}
</style>
