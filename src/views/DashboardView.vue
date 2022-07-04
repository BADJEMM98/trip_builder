<template>
  <div v-if="isLoggedIn" class="container">
    <div class="row">
      <city-select
        label="Ville de départ"
        :index="0"
        @select="addCoordinates"
      ></city-select>
      <div class="input-container">
        <label for="start_date">Date de départ</label>
        <input type="date" id="start_date" />
      </div>
      <div class="input-container">
        <label for="end_date">Date d'arrivée</label>
        <input type="date" id="end_date" />
      </div>
      <div class="input-container">
        <label for="amount">Budget</label>
        <input type="number" id="amount" min="1" step="any" />
      </div>
      <button>Rechercher</button>
    </div>
    <div class="row" @click.stop>
      <div v-for="(step, index) in steps" :key="index">
        <city-select
          :label="'Etape ' + (index + 1)"
          :index="index + 1"
          @select="addCoordinates"
        ></city-select>
      </div>
      <button @click="addStep" class="icon-button"></button>
    </div>
  </div>
</template>

<script setup>
import { getAuth, onAuthStateChanged } from "@firebase/auth";
import { onBeforeUnmount } from "@vue/runtime-core";
import { ref } from "@vue/reactivity";
import { useRouter } from "vue-router";
import CitySelect from "@/components/CitySelect.vue";
const router = useRouter();
const isLoggedIn = ref(false);
const auth = getAuth();
const authListener = onAuthStateChanged(auth, function (user) {
  if (user) {
    isLoggedIn.value = true;
  } else {
    alert("You must be logged in to access this page");
    router.push("/");
  }
});
onBeforeUnmount(() => {
  authListener();
});
</script>
<script>
export default {
  components: {
    "city-select": CitySelect,
  },
  data() {
    return {
      steps: [""],
      coordinates: [],
    };
  },
  methods: {
    addStep() {
      this.steps.push("");
    },
    addCoordinates(index, city) {
      this.coordinates[index] = [city.lat, city.lon];
      console.log(this.coordinates[index]);
    },
  },
};
</script>