<template>
  <div>
    <h1>Buyer Page</h1>
    <div v-if="paymentComplete">
      <div v-if="!refundComplete" >
        <p>{{ paymentComplete.message }}</p>
        <button @click="refundPayment">Refund</button>
      </div>
      <div v-else>
        <p>{{ refundComplete.message }}</p>
      </div>
    </div>
    <div v-else>
      <div v-if="paymentDetails">
        <p>Merchant Name: {{ paymentDetails.merchant.name }}</p>
        <p>Amount: {{ paymentDetails.amount }}</p>
        <p>Description: {{ paymentDetails.description }}</p>
        <p>Created At: {{ formatDate(paymentDetails.created_at) }}</p>
        <button @click="completePayment">Pay Now</button>
      </div>
      <div v-else>
        <p>No payment details available.</p>
      </div>
    </div>
  </div> 
</template>

<script>
import axios from 'axios';
import { format } from 'date-fns';

export default {
  name: 'BuyerPage',
  data() {
    return {
      paymentDetails: null,
      paymentComplete: null,
      refundComplete: null
    };
  },
  mounted() {
    const paymentId = this.$route.query.payment_id;
    this.fetchPaymentDetails(paymentId);
  },
  methods: {
    fetchPaymentDetails(paymentId) {
      axios.get(`http://localhost:8000/api/buyer/payment-gateway/${paymentId}/`)
        .then(response => {
          this.paymentDetails = response.data;
        })
        .catch(error => {
          console.error('Error fetching payment details:', error);
        });
    },

    completePayment() {
      const payload = {
        buyer_id: 1
      };
      axios.put(`http://localhost:8000/api/buyer/payment-gateway/${this.paymentDetails.id}/`,payload)
        .then(response => {
          this.paymentComplete = response.data
        })
        .catch(error => {
          console.error('Error completing payment:', error);
        });
    },

    refundPayment() {
    axios.put(`http://localhost:8000/api/buyer/payment-refund/${this.paymentDetails.id}/`)
      .then(response => {
        this.refundComplete = response.data
      })
      .catch(error => {
        console.error('Error refunding payment:', error);
      });
    },
    formatDate(date) {
      return format(new Date(date), 'MMMM d, yyyy HH:mm:ss');
    }
  }
};
</script>