<script>
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let maxLimit = 10;
  let value = maxLimit;

  function updateValue(event) {
    let inputValue = +event.target.value;

    if (inputValue > maxLimit) {
      value = maxLimit;
    } else if (inputValue < 0) {
      value = 0;
    } else {
      value = inputValue;
    }

    dispatch("update", value);
  }
</script>

<div>
  <span>Limit: </span>
  <input type="number" bind:value on:input={updateValue} />
</div>
