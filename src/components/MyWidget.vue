<!-- MyWidget.vue -->
<template>
  <div>
    <v-sheet
      id="home"
      class="d-flex justify-center align-center text-center flex-column"
      color="primary"
      min-height="600"
    >
      <div class="text-h3 font-weight-medium mb-5">
        Welcome To Saludable
      </div>

      <div class="text-h6 font-weight-light mb-5" style="max-width: 468px;">
        We recognized the importance of providing accurate and timely information to individuals seeking healthcare services, including the availability of COVID-19 medications and telehealth options.
      </div>


        <v-btn text="GET STARTED" :id="triggerId" rounded height="55" color="accent" flat />


      <!-- Widget element -->
      <gen-search-widget
        ref="widgetRef"
        configId="a4040031-e7d3-4ea5-90c8-4175513f600f"
        :triggerId="triggerId"
      ></gen-search-widget>


    </v-sheet>
  </div>
</template>

<script>
export default {
  data() {
    return {
      triggerId: "searchWidgetTrigger" // Unique ID for the trigger element
    };
  },
  methods: {
    showWidget() {
      // Call the method to show the widget directly
      this.$refs.widgetRef.showWidget();
    }
  },
  mounted() {
    // Load the widget JavaScript bundle
    const script = document.createElement("script");
    script.src = "https://cloud.google.com/ai/gen-app-builder/client?hl=en_US";
    script.async = true;
    document.body.appendChild(script);
  }
};
</script>

<style>
/* Add any custom styles here */
</style>
