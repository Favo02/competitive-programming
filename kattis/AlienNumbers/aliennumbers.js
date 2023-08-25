var fs = require("fs")
var stdinBuffer = fs.readFileSync(0)
const input = stdinBuffer.toString().split("\n").splice(1)
input.pop()

for (let i = 0; i < input.length; i++) {
  const el = input[i].split(" ")
  console.log(`Case #${i+1}: ${convert(el[0], el[1], el[2])}`)
}

function toDec(num, base) {
  num = num.split("").reverse()

  let decNum = 0
  for (let i = 0; i < num.length; i++) {
    const e = num[i]

    let n = base.indexOf(e) * Math.pow(base.length, i)
    decNum += n
  }

  return decNum
}

function toIndexes(numDec, newBase) {
  const div = newBase.length
  const ind = []

  while (numDec >= div) {
    ind.push(numDec % div)
    numDec = Math.floor(numDec / div)
  }

  ind.push(numDec)

  return ind
}

function toBase(indexes, base) {
  return indexes.map(i => base[i]).reverse().join("")
}

function convert(num, base, newBase) {
  const dec = toDec(num, base)
  const indxs = toIndexes(dec, newBase)
  return toBase(indxs, newBase)
}
