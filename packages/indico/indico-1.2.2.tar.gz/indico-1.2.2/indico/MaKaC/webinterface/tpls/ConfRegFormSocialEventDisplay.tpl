<table class="regFormSectionTable" width="100%" align="left" cellspacing="0">
    <tr>
        <td nowrap class="regFormSectionTitle">${ title }</td>
    </tr>
    % if description:
    <tr>
        <td style="padding: 10px 0 0 15px;">
            <table width="100%">
                <tr>
                    <td align="left"><pre>${ description }</pre></td>
                </tr>
            </table>
        </td>
    </tr>
    % endif
    <tr>
        <td style="padding: 10px 0 0 15px;">
            <table align="left">
                <tr>
                    <td align="left" colspan="2" class="subGroupTitleRegForm" style="padding-bottom:5px;">${ intro }</td>
                </tr>
                ${ socialEvents }
            </table>
        </td>
    </tr>
</table>
