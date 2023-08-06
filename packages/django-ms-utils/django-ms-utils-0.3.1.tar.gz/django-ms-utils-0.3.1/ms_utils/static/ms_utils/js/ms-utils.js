$(function() {

    $('.nav-tabs a').on('click', function(e) {
        e.preventDefault();
        $(this).tab('show');
    });

    $('[data-role=multiselect]').multiSelect({
        selectableHeader: gettext('<p>Not selected</p>'),
        selectionHeader: gettext('<p>Selected</p>'),
    });

    $('[data-role="datepicker"]').daterangepicker({
        autoUpdateInput: false,
        singleDatePicker: true,
        locale: {
            format: DATEPICKER_FORMAT
        }
    }).on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format(DATEPICKER_FORMAT));
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    });

    $('[data-role="datetimepicker"]').daterangepicker({
        autoUpdateInput: false,
        singleDatePicker: true,
        timePicker: true,
        timePicker24Hour: true,
        locale: {
            format: DATETIMEPICKER_FORMAT
        }
    }).on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format(DATETIMEPICKER_FORMAT));
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    });

    $('[data-role="daterangepicker"]').daterangepicker({
        autoUpdateInput: false,
        locale: {
            format: DATEPICKER_FORMAT
        }
    }).on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format(DATEPICKER_FORMAT) + ' - ' + picker.endDate.format(DATEPICKER_FORMAT));
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    });
})
