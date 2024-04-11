<script lang="ts">
	import { onMount } from 'svelte';
	import TextImageInput from '$lib/components/TextImageInput.svelte';
	import LimitNumberInput from '$lib/components/LimitNumberInput.svelte';
	import MultiChoiceDropdown from '$lib/components/MultiChoiceDropdown.svelte';
	import { getPlacesImpl } from '$lib/services/Places';
	import type { DropdownElem } from '$lib/structs/DropdownElem';

	function handleUpdate(event: any) {
		console.log(event.detail);
	}

	let options: DropdownElem[] | undefined = undefined;

	const placesapi = getPlacesImpl();

	onMount(async () => {
		const rawoptions = await placesapi.getAreas();
		options = rawoptions.map<DropdownElem>((e) => ({ id: e.id, name: e.name, selected: false }));
	});
</script>

<main>
	<TextImageInput />
	{#if options === undefined}
		<p>Loading...</p>
	{:else}
		<MultiChoiceDropdown {options} />
	{/if}
	<LimitNumberInput on:update={handleUpdate} />
</main>

<style>
	main {
		padding: 1rem;
		font-family: Arial, sans-serif;
	}
</style>
