document.addEventListener('keydown', function (event) {
  if (event.code === 'F1') {
    window.location.href = 'http://localhost:5000';
  } else if (event.code === 'F2') {
    window.location.href = 'http://localhost:5000/voxel';
  }
});
