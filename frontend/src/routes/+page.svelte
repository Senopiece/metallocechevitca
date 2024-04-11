<script lang="ts">
	import { onMount } from 'svelte';
	import TextImageInput from '$lib/components/TextImageInput.svelte';
	import LimitNumberInput from '$lib/components/LimitNumberInput.svelte';
	import MultiChoiceDropdown from '$lib/components/MultiChoiceDropdown.svelte';
	import { getPlacesImpl } from '$lib/services/Places';
	import type { DropdownElem } from '$lib/structs/DropdownElem';
	import type { MultimodalSelected } from '$lib/structs/MultimodalSelect';
	import { goto } from '$app/navigation';
	import { searchResultsStore } from '$lib/services/SearchResultStore';

	const placesapi = getPlacesImpl();

	let initialOptions: DropdownElem[] | undefined;

	let limit: number | undefined;
	let selected: MultimodalSelected | undefined;
	let selectedOptionsIds: number[] | undefined;

	function handleSelect(event: CustomEvent<MultimodalSelected>) {
		selected = event.detail;
	}

	function handleUpdate(event: CustomEvent<number>) {
		limit = event.detail;
	}

	function handleSelectedOptions(event: CustomEvent<number[]>) {
		selectedOptionsIds = event.detail;
	}

	async function handleSubmit() {
		if (
			limit === undefined ||
			selected === undefined ||
			initialOptions === undefined ||
			selectedOptionsIds === undefined
		) {
			console.error('All fields are required.');
			console.log(limit, selected, initialOptions, selectedOptionsIds);
			return;
		}

		if (selectedOptionsIds.length === 0) {
			console.error('No areas selected.');
			return;
		}

		let searchResult; // This should be either SearchResultsStoreImage or SearchResultsStoreText based on API call

		if (selected.type === 'text') {
			searchResult = await placesapi.searchText(selected.value, selectedOptionsIds, limit);
			searchResultsStore.set({ type: 'text', res: searchResult });
		} else if (selected.type === 'image') {
			searchResult = await placesapi.searchImage(selectedOptionsIds, selected.file, limit);
			searchResultsStore.set({ type: 'image', image: selected.file, res: searchResult });
		}

		goto('/searchResults');
	}

	onMount(async () => {
		const rawoptions = await placesapi.getAreas();
		initialOptions = rawoptions.map<DropdownElem>((e) => ({
			id: e.id,
			name: e.name,
			selected: false
		}));
	});
</script>

<main>
	<TextImageInput on:selected={handleSelect} />
	<div class="inputs-row">
		{#if initialOptions === undefined}
			<p>Загрузка...</p>
		{:else}
			<MultiChoiceDropdown options={initialOptions} on:selected={handleSelectedOptions} />
		{/if}
		<LimitNumberInput on:update={handleUpdate} />
	</div>
	<button on:click={handleSubmit}>Искать</button>
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		justify-content: center; /* Center vertically */
		align-items: center; /* Center horizontally */
		min-height: 100vh; /* Full height of the viewport */
		padding: 1rem;
		font-family: Arial, sans-serif;
	}

	.inputs-row {
		display: flex;
		justify-content: space-around; /* Adjust this as needed */
		align-items: center; /* Centers items vertically within the row */
		width: 100%;
		max-width: 600px; /* Adjust based on your design */
		margin: 1rem 0; /* Adds margin around the row for spacing */
	}

	button {
		margin-top: 1rem;
	}

	p {
		text-align: center;
	}
</style>
