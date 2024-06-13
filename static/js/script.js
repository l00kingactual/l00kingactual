
$(document).ready(function() {
    const channelDataElement = document.getElementById('channelData');
    if (channelDataElement) {
        const channelDataStr = channelDataElement.dataset.channel;
        console.log("JSON String:", channelDataStr);  // Debugging line
        if (channelDataStr && channelDataStr.trim() !== '') {
            try {
                const channel_data = JSON.parse(channelDataStr);
                const frequencies = {};

                for (const [channel, freqs] of Object.entries(channel_data)) {
                    frequencies[channel] = Object.keys(freqs);
                }

                function populateFrequencies(channel) {
                    $('#frequenciesRow').empty();
                    frequencies[channel].forEach(function(frequency) {
                        $('#frequenciesRow').append(`
                            <div class="col-md-3" id="frequency-${frequency}">
                                <h5>${frequency} Frequency</h5>
                                <button class="btn btn-primary upload-btn" data-frequency="${frequency}">Upload</button>
                                <ul class="file-list" id="file-list-${channel}-${frequency}"></ul>
                            </div>
                        `);
                    });
                }

        function populateFrequencies(channel) {
            $('#frequenciesRow').empty();
            frequencies[channel].forEach(function(frequency) {
                $('#frequenciesRow').append(`
                    <div class="col-md-3" id="frequency-${frequency}">
                        <h5>${frequency} Frequency</h5>
                        <button class="btn btn-primary upload-btn" data-frequency="${frequency}">Upload</button>
                        <ul class="file-list" id="file-list-${channel}-${frequency}"></ul>
                    </div>
                `);
            });
        }

        populateFrequencies($('#channel').val());

        $('#channel').change(function() {
            const newChannel = $(this).val();
            populateFrequencies(newChannel);
        });

        $('#frequenciesRow').on('click', '.upload-btn', function() {
            const frequency = $(this).data('frequency');
            const channel = $('#channel').val();
            $('#fitsFile').data('frequency', frequency);
            $('#fitsFile').data('channel', channel);
            $('#fitsFile').click();
        });

        $('#fitsFile').change(function() {
            const frequency = $(this).data('frequency');
            const channel = $(this).data('channel');
            const files = $(this)[0].files;
            const fileList = $(`#file-list-${channel}-${frequency}`);
            fileList.empty();

            Array.from(files).forEach(function(file, index) {
                const formData = new FormData();
                formData.append('fitsFile', file);
                formData.append('channel', channel);
                formData.append('frequency', frequency);

                const reader = new FileReader();

                reader.onload = function(e) {
                    $.ajax({
                        url: '/upload',
                        type: 'POST',
                        data: formData,
                        contentType: false,
                        processData: false,
                        success: function(response) {
                            if (response.status === 'success') {
                                fileList.append(`
                                    <li>
                                        <div>${file.name}</div>
                                        <img src="data:image/png;base64,${response.img_base64}" width="50" height="50" alt="Preview">
                                    </li>
                                `);
                            }
                        },
                        error: function(jqXHR, textStatus, errorThrown) {
                            console.log('Upload failed.', jqXHR, textStatus, errorThrown);
                        }
                    });
                };
                reader.readAsDataURL(file);
            });
        });

        $('#stackAlignBtn').click(function() {
            const channel = $('#channel').val();
            $.post('/stack_and_align', { channel: channel }, function(response) {
                if (response.status === 'success') {
                    $('#imagePreview').html(`<img src="data:image/png;base64,${response.img_base64}" width="1000" height="1000" alt="Preview">`);
                }
            });
        });

        $('#saveImageBtn').click(function() {
            const channel = $('#channel').val();
            $.post('/save_image', { channel: channel }, function(response) {
                if (response.status === 'success') {
                    alert('Image saved successfully.');
                }
            });
        });
    
    } catch (e) {
        console.error('Error parsing JSON:', e);
    }
        } else {
            console.error('channelData is empty or undefined');
        }
        } else {
        console.error('Element with id channelData not found');
        }
}); 