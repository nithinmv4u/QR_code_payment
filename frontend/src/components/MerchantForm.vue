<template>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" v-model="paymentDetails.amount" required>
      </div>
      <br>
      <div>
        <label for="description">Description:</label>
        <input type="text" id="description" v-model="paymentDetails.description" required>
      </div>
      <br>
      <button type="submit">Generate QR Code</button>
    </form>
  </template>
  
  <script>
  export default {
    name: 'MerchantForm',
    data() {
      return {
        paymentDetails: {
          amount: null,
          description: ''
        }
      }
    },
    methods: {
      handleSubmit() {
        this.$emit('submit-payment', this.paymentDetails)
      }
    }
  }
  </script>
  