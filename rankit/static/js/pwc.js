const pool = document.querySelector('#top')
const high = document.querySelector('#high')
const low = document.querySelector('#low')

const containers = [
  pool,
  high,
  low,
]
dragula(containers, {
  copy: (el, source) => source === pool,
  accepts: (el, target) => target !== pool,
  removeOnSpill: true,
})
