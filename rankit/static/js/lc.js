const source = document.querySelector('#top')
const target = document.querySelector('#center')

const source_sortable = Sortable.create(source, {
  group: 'list',
  animation: 300,
  sort: false,
})

const target_sortable = Sortable.create(target, {
  group: 'list',
  animation: 300,
})