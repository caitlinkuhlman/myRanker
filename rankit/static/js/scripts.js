// Empty JS for your own code to be here
const pool = document.querySelector('#top')
const center = document.querySelector('#center')
const left = document.querySelector('#left')
const right = document.querySelector('#right')
const containers = [
  pool,
  center,
  left,
  right,
]
dragula(containers, {
  copy: (el, source) => source === pool,
  accepts: (el, target) => target !== pool,
  removeOnSpill: true,
})
