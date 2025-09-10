<template>
    <h1>Page not found</h1>
</template>

<script>

  export default {
    name: "auth",

    data() {
      return {
        club: null
      }
    },

    methods: {
      
      showTost() {
        this.$toastr.s("Success", "Hello world");
      },
    },


  }
</script>

<style>
</style>