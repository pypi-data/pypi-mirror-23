<form action=${ postURL } method="POST">
    <table width="80%" align="center" border="0" style="border-left: 1px solid #777777">
        <tr>
            <td class="groupTitle" colspan="2">Configuration of yellowPay</td>
        </tr>
        <tr>
            <td nowrap class="dataCaptionTD"><span class="titleCellFormat">Title</span></td>
            <td align="left"><input type="text" name="title" size="60" value="${ title }"></td>
        </tr>
        <tr>
            <td class="dataCaptionTD"><span class="dataCaptionFormat">URL of yellowpay</span></td>
            <td align="left"><input type="text" name="url" size="60" value="${ url }"></td>
        </tr>
        <tr>
            <td class="dataCaptionTD"><span class="dataCaptionFormat">Master Shop ID</span></td>
            <td align="left"><input type="text" name="mastershopid" size="60" value="${ mastershopid }"></td>
        </tr>
        <tr>
            <td class="dataCaptionTD"><span class="dataCaptionFormat">Shop ID</span></td>
            <td align="left"><input type="text" name="shopid" size="60" value="${ shopid }"></td>
        </tr>
        <tr>
            <td class="dataCaptionTD"><span class="dataCaptionFormat">Hash Seed</span></td>
            <td align="left"><input type="text" name="hashseed" size="60" value="${ hashseed }"></td>
        </tr>
        <tr><td>&nbsp;</td></tr>
        <tr>
            <td colspan="2" align="left"><input type="submit" value="OK">&nbsp;<input type="submit" value="cancel" name="cancel"></td>
        </tr>
    </table>
</form>
