<template>
    <div>
      <h2>QR Code:</h2>
      <img :src="qrCodeUrl" alt="QR Code">
    </div>
  </template>
  
  <script>
  export default {
    name: 'QRCodeDisplay',
    props: {
      qrCodeUrl: {
        type: String,
        required: true
      }
    }
  }
  </script>
  