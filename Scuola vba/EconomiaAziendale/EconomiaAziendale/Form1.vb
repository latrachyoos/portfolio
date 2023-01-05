Public Class Form1

    Dim File1 As String = "completamento.txt"
    Dim File2 As String = "merce.txt"
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        carica(File2)
    End Sub

    Structure stcAcqVen
        Dim Valore As Decimal
        Dim Iva As Decimal
        Dim CreDeb As Decimal
    End Structure

    Sub visua(ByVal Ven As Boolean)
        Dim posto As String = "conto"
        Dim i As Byte
        dgv.Rows.Clear()
        For i = 0 To 2
            dgv.Rows.Add()
            If Not Ven Then
                dgv.Rows(i).Cells(posto).Value = script(i)
            Else
                dgv.Rows(i).Cells(posto).Value = script(i + 3)
            End If
        Next
        'Do
        '    dgv.Rows.Add()
        '    If Not Ven Then
        '        dgv.Rows(i).Cells(posto).Value = script(i)
        '    Else
        '        dgv.Rows(i).Cells(posto).Value = script(i + 3)
        '        i += 1
        '        dgv.Rows.Add()
        '        dgv.Rows(i).Cells(posto).Value = script(0)
        '        i += 1
        '        dgv.Rows.Add()
        '        dgv.Rows(i).Cells(posto).Value = script(i + 2)
        '    End If
        '    i += 1
        'Loop Until i > 2
        If Not Ven Then
            dgv.Rows(0).Cells("dare").Value = Scrittura.Valore
            dgv.Rows(1).Cells("dare").Value = Scrittura.Iva
            dgv.Rows(2).Cells("avere").Value = Scrittura.CreDeb
        Else
            dgv.Rows(1).Cells("avere").Value = Scrittura.Valore
            dgv.Rows(2).Cells("avere").Value = Scrittura.Iva
            dgv.Rows(0).Cells("dare").Value = Scrittura.CreDeb
        End If
    End Sub

    Dim Scrittura As stcAcqVen
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnEconomia.Click
        Dim Ven As Boolean = True
        Dim Coef As Single = 0.22
        If radAcq.Checked Then
            Ven = False
        End If
        If IsNumeric(txtVal.Text) Then
            Scrittura.Valore = Trim(txtVal.Text)
            Scrittura.Iva = Scrittura.Valore * Coef
            calcoli()
            completamento(File1, Ven)
            visua(Ven)
        End If
    End Sub

    Sub calcoli()
        Scrittura.CreDeb = Scrittura.Iva + Scrittura.Valore
    End Sub

    Dim script(9) As String
    Sub completamento(ByVal F As String, ByVal Ven As Boolean)
        Dim Ns As Integer
        FileOpen(1, F, OpenMode.Input)
        Do While Not EOF(1)
            script(Ns) = LineInput(1)
            Ns += 1
        Loop
        If Trim(cmbScrit.Text) <> "" Then
            script(0) = Trim(cmbScrit.Text)
            script(4) = Trim(cmbScrit.Text)
        End If
        FileClose(1)
    End Sub

    Sub carica(ByVal F As String)
        FileOpen(2, F, OpenMode.Input)
        Do While Not EOF(2)
            cmbScrit.Items.Add(LineInput(2))
        Loop

        FileClose(2)
    End Sub
End Class
