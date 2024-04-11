<script lang="ts">
	import type { DropdownElem } from '$lib/structs/DropdownElem';
	import { createEventDispatcher, onDestroy, onMount } from 'svelte';

	let dropdownElement;

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

	const handleClickOutside = (event) => {
		if (!dropdownElement.contains(event.target)) {
			isDropdownOpen = false;
		}
	};

	onMount(() => {
		dispatch('selected', selectedIds);
		window.addEventListener('click', handleClickOutside);
	});

	onDestroy(() => {
		window.removeEventListener('click', handleClickOutside);
	});

	function handleDropdownClick(event) {
		// Prevent click inside dropdown from reaching window
		event.stopPropagation();
	}

	$: selectedIds = options.filter((option) => option.selected).map((option) => option.id);
	$: options, dispatchSelectedOptions();
	$: allSelected = options.every((option) => option.selected && options.length > 0);
</script>

<div class="dropdown" bind:this={dropdownElement} on:click={handleDropdownClick}>
	<span on:click={() => (isDropdownOpen = !isDropdownOpen)}
		>Выбрать города {isDropdownOpen ? '▲' : '▼'}</span
	>
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
	button {
		background-color: #f9f9f9; /* Light gray background */
		color: #333; /* Dark text for better readability */
		border: 1px solid #ccc; /* Light border for a flat look */
		padding: 8px 16px;
		font-size: 16px;
		border-radius: 4px; /* Slightly rounded corners */
		cursor: pointer;
		outline: none;
		transition:
			background-color 0.2s,
			box-shadow 0.2s,
			border-color 0.2s;
	}

	button:hover,
	button:focus {
		background-color: #e8e8e8; /* Slightly darker on hover/focus */
		border-color: #bbb; /* Darker border on hover/focus */
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
	}

	.dropdown-menu {
		border: 1px solid #ccc;
		border-radius: 4px; /* Match button corners */
		padding: 10px;
		margin-top: 5px;
		background: white;
		position: absolute;
		width: max-content; /* Adjust width to content */
		max-width: 100%; /* Prevent overflow */
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for pop-out effect */
		z-index: 1000; /* Ensure dropdown appears above other content */
	}

	label {
		display: flex;
		align-items: center;
		cursor: pointer;
		margin: 5px 0; /* Spacing between options */
	}

	input[type='checkbox'] {
		margin-right: 8px; /* Space between checkbox and label text */
	}

	/* Style tweaks for better touch interaction */
	input[type='checkbox'] {
		transform: scale(1.2);
		margin-right: 10px;
	}

	.dropdown {
		position: relative;
		font-family: 'Arial', sans-serif; /* Using Arial as a placeholder for generic sans-serif */
	}

	span {
		color: #007bff; /* Link-like blue color */
		cursor: pointer;
		display: inline-flex;
		align-items: center;
		font-family: sans-serif; /* Ensuring the chevron uses the same sans-serif font */
		font-size: 16px; /* Adjust size as needed */
	}

	.dropdown-menu {
		font-family: sans-serif;
		border: 1px solid #ccc;
		border-radius: 4px;
		padding: 10px;
		margin-top: 5px;
		background: white;
		position: absolute;
		width: max-content;
		max-width: 100%;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		z-index: 1000;
	}
</style>
