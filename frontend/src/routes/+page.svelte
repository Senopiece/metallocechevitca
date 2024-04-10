<script lang="ts">
	import { onMount } from 'svelte';
	import TextImageInput from '$lib/components/TextImageInput.svelte';
	import LimitNumberInput from '$lib/components/LimitNumberInput.svelte';
	import MultiChoiceDropdown from '$lib/components/MultiChoiceDropdown.svelte';
	import { getPlacesImpl } from '$lib/services/Places';
	import type { DropdownElem } from '$lib/structs/DropdownElem';
	import type { MultimodalSelected } from '$lib/structs/MultimodalSelect';

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

		if (selected.type === 'text') {
			const searchResult = await placesapi.searchText(selected.value, selectedOptionsIds, limit);
			console.log(searchResult);
		} else if (selected.type === 'image') {
			const searchResult = await placesapi.searchImage(selectedOptionsIds, selected.file, limit);
			console.log(searchResult);
		}
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
	{#if initialOptions === undefined}
		<p>Загрузка...</p>
	{:else}
		<MultiChoiceDropdown options={initialOptions} on:selected={handleSelectedOptions} />
	{/if}
	<LimitNumberInput on:update={handleUpdate} />
	<button on:click={handleSubmit}>Искать</button>
</main>

<style>
	main {
		padding: 1rem;
		font-family: Arial, sans-serif;
	}
</style>
