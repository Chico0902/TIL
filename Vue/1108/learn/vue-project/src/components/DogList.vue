<template>
    <div class="header">
        <h2>랜덤 강아지 가챠</h2>
        <button @click="getRandomDogData" class="styled-button">새로운 강아지 뽑기</button>
    </div>
    <div v-if="dogIsEmpty" class="dog-container">
    <div v-for="dog in dogs" class="dog-box">
        <!-- 하위 컴포넌트로 분리해보기 -->
        <!-- <DogDetail /> -->
        <img :src="dog.url" alt="" >
        <div v-if="dog.detail" class="dog-info">
        <p><strong>이름:</strong>{{ dog.detail.name }}</p>
        <p><strong>품종:</strong>{{ dog.detail.breed_group }}</p>
        <p><strong>높이:</strong>{{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }}cm)</p>
        <p><strong>수명:</strong>{{ dog.detail.life_span }}</p>
        <p><strong>성격:</strong>{{ dog.detail.temperament }}</p>
        <p><strong>무게:</strong>{{ dog.detail.weight.imperial }} 파운드({{ dog.detail.weight.metric }}kg)</p>
        </div>
        <div v-else class="dog-info">
            상세 정보 없음
        </div>
    </div>
</div>
<div v-else>
    아직 데이터를 받아오지 않았다.
</div>
</template>

<script setup>
import { computed, watch } from 'vue';

const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
    emit('getDogData')
}
const props = defineProps({
    dogs: Array
})

watch(props,() => {
    console.log('in props')
})

const dogIsEmpty = computed(() => {
    // script 에서는 props.<변수>로 접근해야 한다
    return props.dogs.length > 0 ? true : false
})
</script>

<style scoped>
.header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.styled-button {
      background-color: #3498db; /* 배경색 */
      color: #fff; /* 글자색 */
      padding: 10px 20px; /* 내부 여백 */
      border: none; /* 테두리 없음 */
      border-radius: 5px; /* 둥근 모서리 */
      cursor: pointer; /* 포인터 커서 */
      font-size: 16px; /* 글꼴 크기 */
    }
      /* 버튼 호버 효과 */
      .styled-button:hover {
      background-color: #2375b3; /* 호버 시 배경색 변경 */
    }

    .dog-container{
        border: 1px solid #000;
        margin:10px;
        border-radius: 10px;
    }
    .dog-box{
        border: 1px solid #000;
        margin: 10px;
        border-radius: 10px;
        display: flex;
        
    }
    .dog-box img{
        width: 200px;
        height: 200px;
        object-fit: fill;
        border-radius: 10px;
    }
    .dog-info {
        margin-left: 10px;
    }
</style>