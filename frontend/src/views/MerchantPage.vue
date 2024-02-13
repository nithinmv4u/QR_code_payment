<template>
  <div class='merchant-page'>
    <h1>Merchant Payment Page</h1>
    <merchant-form v-if="!qrCodeUrl" @submit-payment="submitPayment" />
    <q-r-code-display v-if="qrCodeUrl" :qrCodeUrl="qrCodeUrl" />
  </div>
</template>

<script>
import MerchantForm from '@/components/MerchantForm.vue'
import QRCodeDisplay from '@/components/QRCodeDisplay.vue'
import axios from 'axios'

export default {
  name: 'MerchantPage',
  components: {
    MerchantForm,
    QRCodeDisplay
  },
  data () {
    return {
      qrCodeUrl: null
    }
  },
  methods: {
    async submitPayment (paymentDetails) {
      try {
        const merchantData = {
          merchant: 1,
        }
        const requestData = {
          ...paymentDetails,
          ...merchantData
        }
        const response = await axios.post(
          'http://127.0.0.1:8000/api/merchant/generate_qr_code/',
          requestData
        )
        localStorage.setItem('qrCodeUrl', response.data.qr_code_img)
        this.qrCodeUrl = `data:image/png;base64,${response.data.qr_code_img}`
        console.log(this.qrCodeUrl);
      } catch (error) {
        console.error('Error creating payment link:', error)
      }
    }
  }
}
</script>
