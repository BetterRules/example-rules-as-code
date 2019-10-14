const beardExamples = require('../../shared/example_beards.json');

function hasABeard(facial_hair_over_limit, on_or_below_chin, uninterrupted_below_nose) {
  return facial_hair_over_limit && (on_or_below_chin || uninterrupted_below_nose);
}

const beardData = beardExamples.map(function(beard){
  let data = {}
  data.facial_hair_over_limit = beard.facial_hair_over_5mm
  data.on_or_below_chin = beard.facial_hair_on_or_below_chin
  data.uninterrupted_below_nose = beard.facial_hair_uninterrupted
  data.outcome = beard.outcome
  return(data)
})

let passed_tests = [];
let failed_tests = [];

beardData.forEach(function(beard){
  let result = hasABeard(beard.facial_hair_over_limit, beard.on_or_below_chin, beard.uninterrupted_below_nose);
  if(String(result) == String(beard.outcome)){
    console.log("✅")
    passed_tests.push(beard)
  } else {
    console.log("❌")
    failed_tests.push(beard)
  }
})

console.log(passed_tests.length + ' tests passed')
console.log(failed_tests.length + ' tests failed')

failed_tests.forEach(function(test){
  console.log('Failed this beard:')
  console.log(test)
});

// console.log(beardExamples);
