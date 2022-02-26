// Show/hide the boolean field `is_pr_manager`.
// The field has to be extended in admin with CSS class `depended_on_team`.
//
// The logic:
//  - show the field if selected team type is `art`
//  - set "checked" to `false` and hide the field if other partner type is selected

jQuery(document).ready(function ($) {
    let teamTypeSelectField = $("#id_team");
    let divDependedOnTeamType = $(".depended_on_team_type");

    function toggleDivDependedOnTeamType(teamType) {
        if (teamType === "art") {
            divDependedOnTeamType.slideDown();
        } else {
        divDependedOnTeamType.slideUp();
        }
    }

    // show/hide on load based on existing value of teamTypeSelectField
    toggleDivDependedOnTeamType(teamTypeSelectField.val(), true);

    // show/hide on change
    teamTypeSelectField.change(function () {
        toggleDivDependedOnTeamType($(this).val(), false);
    });
});
