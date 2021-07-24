const friendsList = document.getElementById('friends-dropdown')
const friendsListBtn = document.getElementById('friends-dropdown-btn')

friendsListBtn.addEventListener('click', () => {
    friendsList.classList.toggle('active')
    friendsListBtn.classList.toggle('active')
})

