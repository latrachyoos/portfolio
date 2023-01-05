Public Class formprodottielenco

    Private Sub dgv_CellContentClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgv.CellContentClick

    End Sub

    Private Sub formprodottielenco_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        uptadedgv(dgv, "select * from prodotti where idprodotto = 200")
    End Sub
End Class