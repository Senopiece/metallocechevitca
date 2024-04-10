import type { SearchResultsStore } from '$lib/structs/SerachResult';
import { writable } from 'svelte/store';

export const searchResultsStore = writable<SearchResultsStore | null>(null);
