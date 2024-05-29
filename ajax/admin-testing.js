$(document).ready(function () {
    $("#carmakers").change(function () {
        var select = document.getElementById('carmakers');
        var value = select.options[select.selectedIndex].value;
        $.ajax({
            type: 'GET',
            url: '/project_admin/carmakerdropdown/',
            data: {
                'maker':value
            },
            success: function (response) {
                console.log('success', response.data)
                var lbl = document.getElementById('#carname');
                const data = response.data;
                var selOpts = "<option selected='selected' disabled>select Cars</option>";
                $.each(data, function(k, v)
            {
                // var id = data[k].carid;
                var val = data[k].carname;
                    console.log('cars :', val)
                    selOpts += "<option value='"+val+"'>"+val+"</option>";
            });
                document.getElementById("cars").innerHTML = selOpts;
            },
            error: function (error) {
                console.log('error',error)
            }
        })
        console.log(value);
        console.log("working :",value);
    });
});