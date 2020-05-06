function opentab(evt, tabName) {
    var i, x, tabBtns;
    x = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    tabBtns = document.getElementsByClassName("tabBtn");
    for (i = 0; i < x.length; i++) {
      tabBtns[i].className = tabBtns[i].className.replace(" tab-Active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " tab-Active";
  }