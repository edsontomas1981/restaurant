const carrega_sidebar = ()=>{
	let sidebar = document.getElementById("sidebar")
	sidebar.innerHTML = html_sidebar()
}

const html_sidebar = ()=>{
	return `
  <div class="user-info">
    <img src="images/face.jpg" alt="">
    <p class="name">Richard V.Welsh</p>
    <p class="designation">Manager</p>
    <span class="online"></span>
  </div>
  <ul class="nav">
    <li class="nav-item active">
      <a class="nav-link" href="index.html">
        <img src="images/icons/1.png" alt="">
        <span class="menu-title">Dashboard</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/widgets.html">
        <img src="images/icons/2.png" alt="">
        <span class="menu-title">Widgets</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/forms/index.html">
        <img src="images/icons/005-forms.png" alt="">
        <span class="menu-title">Forms</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/ui-elements/buttons.html">
        <img src="images/icons/4.png" alt="">
        <span class="menu-title">Buttons</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/tables/index.html">
        <img src="images/icons/5.png" alt="">
        <span class="menu-title">Tables</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/charts/index.html">
        <img src="images/icons/6.png" alt="">
        <span class="menu-title">Charts</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/icons/index.html">
        <img src="images/icons/7.png" alt="">
        <span class="menu-title">Icons</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="pages/ui-elements/typography.html">
        <img src="images/icons/8.png" alt="">
        <span class="menu-title">Typography</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" data-toggle="collapse" href="#sample-pages" aria-expanded="false" aria-controls="sample-pages">
        <img src="images/icons/9.png" alt="">
        <span class="menu-title">Sample Pages<i class="fa fa-sort-down"></i></span>
      </a>
      <div class="collapse" id="sample-pages">
        <ul class="nav flex-column sub-menu">
          <li class="nav-item">
            <a class="nav-link" href="pages/samples/blank_page.html">
              Blank Page
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="pages/samples/login.html">
              Login
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="pages/samples/register.html">
              Register
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="pages/samples/404.html">
              404
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="pages/samples/500.html">
              500
            </a>
          </li>
        </ul>
      </div>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">
        <img src="images/icons/10.png" alt="">
        <span class="menu-title">Settings</span>
      </a>
    </li>
  </ul>
`
}

carrega_sidebar()

