const login = document.getElementById('login-box')
const needAcc = document.getElementById('no-acc')
const signin = document.getElementById('signin-box')

needAcc.addEventListener('click', ()=>{
    login.classList.toggle('active')
    needAcc.classList.toggle('active')
    signin.classList.toggle('active')
})