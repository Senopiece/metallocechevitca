<script lang="ts">
	import type { DropdownElem } from '$lib/structs/DropdownElem';
	import { createEventDispatcher, onMount } from 'svelte';

	export let options: DropdownElem[] = [];
	let isDropdownOpen = false;

	const dispatch = createEventDispatcher<{
		selected: number[];
	}>();

	function toggleSelectAll() {
		const newSelectionValue = !allSelected;
		options = options.map((option) => ({
			...option,
			selected: newSelectionValue
		}));
		dispatchSelectedOptions();
	}

	// Dispatch the IDs of the selected options
	function dispatchSelectedOptions() {
		dispatch('selected', selectedIds);
	}

	onMount(() => {
		dispatch('selected', selectedIds);
	});

	$: selectedIds = options.filter((option) => option.selected).map((option) => option.id);
	$: options, dispatchSelectedOptions();
	$: allSelected = options.every((option) => option.selected && options.length > 0);
</script>

<div class="dropdown">
	<button on:click={() => (isDropdownOpen = !isDropdownOpen)}> Выбрать города </button>
	{#if isDropdownOpen}
		<div class="dropdown-menu">
			<label>
				<input type="checkbox" checked={allSelected} on:change={toggleSelectAll} />
				Выбрать все
			</label>
			{#each options as option}
				<label>
					<input
						type="checkbox"
						bind:checked={option.selected}
						on:change={dispatchSelectedOptions}
					/>
					{option.name}
				</label>
			{/each}
		</div>
	{/if}
</div>

<style>
	.dropdown-menu {
		border: 1px solid #ccc;
		padding: 10px;
		margin-top: 5px;
		background: white;
		position: absolute;
	}
	label {
		display: block;
		cursor: pointer;
	}
	button {
		cursor: pointer;
	}
</style>
