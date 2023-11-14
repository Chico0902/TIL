const sayT1 = () => {
    console.log('T1이 최고야!')
  }
  
  const sayDongHyeon = () => {
    console.log('징동 DOWN!')
  }
  
  // - 전역 객체로, js 파일이 모듈 역할을 할 수 있도록 
  // console.log(module)
  // module.exports = {sayT1, sayDongHyeon}
  export {sayT1, sayDongHyeon}
  