<template>
  <div class="about">
    <br />
    <form
      @keyup="onKeyUp"
      v-on:submit.prevent="getSymbolData()"
    >
      <div class="mb-6">
        <label for="symbol" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Symbol to search</label
        >
        <input
          autofocus
          type="text"
          id="symbol"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="ZSK2024"
          required
          v-model="form.symbol"
        />
      </div>
    </form>

    <div v-if="symbolDataJson" class="relative overflow-x-auto shadow-md sm:rounded-lg mb-12">
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400" border="1">
        <thead
          class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
        >
          <tr>
            <th scope="col" class="px-6 py-3">Symbol</th>
            <th scope="col" class="px-6 py-3">Description</th>
            <th scope="col" class="px-6 py-3">Type</th>
            <th scope="col" class="px-6 py-3">Exchange</th>
            <th scope="col" class="px-6 py-3">Currency Code</th>
          </tr>
        </thead>
        <tbody>
          <tr
            class="bg-white border-b dark:bg-gray-900 dark:border-gray-700"
            :key="obj.symbol + obj.description"
            v-for="obj in symbolDataJson"
          >
            <td class="px-6 py-4">{{ obj.symbol }}</td>
            <td class="px-6 py-4">{{ obj.description }}</td>
            <td class="px-6 py-4">{{ obj.type }}</td>
            <td class="px-6 py-4">{{ obj.exchange }}</td>
            <td class="px-6 py-4">{{ obj.currency_code }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',

  data() {
    return {
      // msg: '',
      form: {
        symbol: ''
      },
      symbolData: null,
      symbolDataJson: null
    }
  },

  methods: {
    // getMessage() {
    //   const path = 'http://localhost:5003/ping'
    //   axios
    //     .get(path)
    //     .then((res) => {
    //       this.msg = res.data
    //     })
    //     .catch((error) => {
    //       console.error(error)
    //     })
    // },

    onKeyUp(event) {
      if (this.form.symbol.length < 2) {
        // console.log(this.form.symbol.length)
        return
      }

      this.getSymbolData()
    },

    getSymbolData() {
      if (this.form.symbol.length < 2) {
        return
      }

      const path = 'http://localhost:5003/symbol_search'
      axios
        .post(path, {
          symbol: this.form.symbol
        })
        .then((res) => {
          this.symbolData = res.data
          // console.log(typeof(this.symbolData));
          this.symbolDataJson = JSON.parse(this.symbolData)
          this.symbolDataJson.forEach(function (entry) {
            console.log(entry)
          })
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },

  created() {
    // this.getMessage()
    // this.getSymbolData()
  }
}
</script>

<style></style>
