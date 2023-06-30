$(document).ready(function() {
  $('#id_post_type').change(function() {
    var selectedType = $(this).val();
    if (selectedType === 'text') {
      $('#text_fields').show();
      $('#image_fields').hide();
      $('#video_fields').hide();
    } else if (selectedType === 'image') {
      $('#text_fields').hide();
      $('#image_fields').show();
      $('#video_fields').hide();
    } else if (selectedType === 'video') {
      $('#text_fields').hide();
      $('#image_fields').hide();
      $('#video_fields').show();
    } else {
      $('#text_fields').hide();
      $('#image_fields').hide();
      $('#video_fields').hide();
    }
  });
});
