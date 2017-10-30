// Empty JS for your own code to be here
const pool = document.querySelector('#top')
const bot = document.querySelector('#bot')
const containers = [
  pool,
  bot,
]
dragula(containers, {
  copy: (el, source) => source === pool,
  accepts: (el, target) => target !== pool,
  removeOnSpill: true,
})
