var fs = require("fs")
var stdinBuffer = fs.readFileSync(0)
const input = stdinBuffer.toString().split("\n").splice(1)
input.pop()

const newSeqs = []

for (let i = 0; i < input.length; i+=2) {
  
  const element = input[i+1]
  const arr = element.split(" ").map(e => parseInt(e))

  // console.log(arr)
  
  const newArr = []
  newArr.push(arr[0])

  for (let j = 1; j < arr.length; j++) {
    if (arr[j] >= arr[j-1]) {
      newArr.push(arr[j])
    }
    else {
      newArr.push(arr[j])
      newArr.push(arr[j])
    }  
  }
  
  newSeqs.push(newArr)
}

// console.log(newSeqs)


for (let i = 0; i < newSeqs.length; i++) {
  console.log(newSeqs[i].length)
  console.log(newSeqs[i].join(" "))
}
