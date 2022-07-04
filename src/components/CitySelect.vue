<template>
  <div class="input-container">
    <label for="start">{{ label }}</label>
    <div class="input-with-options">
      <input
        type="text"
        id="start"
        @input="autocomplete"
        v-model="selectedCity"
      />
      <div class="options">
        <div v-for="(city, index) in cities" :key="index" @click="select(city)">
          {{ city.city }}, {{ city.state }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    label: String,
    index: Number,
  },
  emits: ["select"],
  data() {
    return {
      cities: [],
      selectedCity: "",
    };
  },
  methods: {
    autocomplete(event) {
      let value = event.target.value;
      if (value.length > 3) {
        fetch(
          "https://api.geoapify.com/v1/geocode/autocomplete?text=" +
            event.target.value +
            "&type=city&format=json&apiKey=feceeb3dfed2472f961e5a5f8eb546aa"
        )
          .then((res) => {
            return res.json();
          })
          .then((value) => {
            this.cities = value.results;
          });
      }
    },
    select(city) {
      this.selectedCity = city.city + ", " + city.state;
      this.cities = [];
      this.$emit("select", this.index, city);
    },
  },
};
</script>