Public Class Form1
    Dim contlenmin5 As Integer
    Private Sub btnaggiungi_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnaggiungi.Click
        If txtname.Text <> "" Then
            If UCase(txtname.Text) <> "STOP" Then
                If Len(txtname.Text) <= 5 Then
                    contlenmin5 += 1
                End If
                txtname.Text = ""
            Else
                txtcont.Text = contlenmin5
            End If
        Else
            MessageBox.Show("INSERISCI UN VALORE VALIDO")
        End If
    End Sub
End Class
