import { getPlacesImpl } from '$lib/services/Places';

export async function load({}) {
	const placesapi = getPlacesImpl();
	const options = await placesapi.getAreas();

	return {
		props: {
			options: options
		}
	};
}
