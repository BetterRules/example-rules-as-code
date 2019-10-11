const jsonLogic = require("./logic");
const beardExamples = require("../../shared/example_beards.json");
const beardRules = require("../beard_definition.json");

const beardData = beardExamples.map(function(beard){
  let data = {}

  data.on_or_below_chin = beard.facial_hair_on_or_below_chin
  data.uninterrupted_below_nose = beard.facial_hair_uninterrupted
  data.facial_hair_over_limit = beard.facial_hair_over_5mm
  data.outcome = beard.outcome
  return(data)
})

let passed_tests = [];
let failed_tests = [];

beardData.forEach(function(beard){
  let result = jsonLogic.apply(beardRules, beard)
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
