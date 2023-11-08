<template>
  <div class="container">
    <h1>2023-11-08 실습</h1>
    <!-- Doglist -->
    <DogList :dogs="dogs" @get-dog-data="getDogData"/>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import DogList from './components/DogList.vue';
import axios from 'axios'

const dogs = ref([])

// async : 이 함수가 비동기 함수다 알려주는 키워드
// await : 비동기 함수의 종료를 기다려주는 키워드
// try-catch 와 함께 자주 사용된다.

const getDogData = async() => {
  const URL = 'https://api.thedogapi.com/v1/images/search?limit=10'

  // 비동기 버그 해결 코드
  try {
    const response = await axios.get(URL)

    const dogData = response.data

    // 암기1. 비동기 쓸 때 forEach 쓰지 말자!
      //  map 으로 변경! -> map : 기존 데이터 토대로 새로운 배열 반환 
    // 암기2. map안에 async쓰면 자동으로 Promise 객체 반환됨
    const details = dogData.map(async (dog) => {
      const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
      const detailres = await axios.get(detailURL)
      dog.detail = detailres.data.breeds ? detailres.data.breeds[0] : null
    })
    // Promise 객체 10개가 출력됨 = 상태가 : fulfilled(성공함)
    // Promise 실행 자체는 성공했는데 
    // 순서는 보장하지 못했다!
    console.log(details)


    // Promise.all : Promise 배열의 계산이 모두 끝날때까지 기다려줌
    await Promise.all(details)


    dogs.value = dogData
    console.log(dogData)

  } catch(error) {
    console.log('강아지 데이터 못불러옴',error)
  }
}




// 비동기 버그있는 코드
  //   axios.get(url)
//   .then((response) =>{
//     // dogs.value = Response.data

//     // 10마리 강아지 데이터
//     const dogData = response.data
    
//     dogData.forEach((dog) => {
//       const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
//       axios.get(detailURL)
//       .then((response) => {
//         // console.log('detail = ', response.data)
//         dog.detail = response.data
//       }).catch((error) => {
//         console.error(error)
//       })
//     })
//     dogs.value = dogData
//     console.log(response)
//   }).catch((error) => {
//     console.error(error)
//   })



// }
    

</script>

<style scoped>
.container{
  width: 80%;
  margin: 0 auto;
}
</style>