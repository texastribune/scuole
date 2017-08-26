const menuSelects = document.querySelectorAll('.menu-select');

for (var i = 0; i < menuSelects.length; i++) {
  const select = menuSelects[i];

  select.addEventListener('change', e => {
    const val = e.target.value;

    if (val === '') return;

    window.location.href = val;
  });
}
