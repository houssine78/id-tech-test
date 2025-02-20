import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.RealEstateWebsiteSale = publicWidget.Widget.extend({
    selector: '.oe_website_sale',
    
    events: {
        'change select[name="real_estate_project"]': '_onChangeProject',
        'click input[name="select_project"]': '_onClickProject',
    },

    start: function () {
        this._super.apply(this, arguments);
    },

    _onChangeProject: function (event) {
        const self = this;
        const $target = $(event.target);

        let $warning_project_completed = self.$el.find('.alert-project-completed');
        $warning_project_completed.addClass('d-none');
        if($target.find('option:selected').data('is-completed')){
             $warning_project_completed.removeClass('d-none');
        }
    },

    _onClickProject: function () {
        var $selected_project_id = $("#real_estate_project").val();

        rpc("/shop/update_project", {
            selected_project_id: $selected_project_id,
        }).then((data) => {
            
        });
    },
});
