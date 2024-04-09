import { getPlacesImpl } from '$lib/services/Places';

export async function load({}) {
	const placesapi = getPlacesImpl();
	const options = await placesapi.getAreas();
	const initDropdownState = options.map<DropdownElem>((e) => {
		return { id: e.id, name: e.name, selected: false };
	});

	return {
		options: initDropdownState
	};
}
